import sys
import numpy as np
import pygame
import Clases

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 200, 200)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
TOOLBAR_HEIGHT = 50
NODE_RADIUS = 20
STEP_DELAY = 300


class Button:
    """A clickable toolbar button tied to a mode or an action."""
    def __init__(self, x, y, width, height, text, mode):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.mode = mode

    def draw(self, screen, font, current_mode):
        color = DARK_GRAY if current_mode == self.mode else GRAY
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        label = font.render(self.text, True, BLACK)
        screen.blit(label, (self.rect.x + 8, self.rect.y + 6))


class AppState:
    """Everything the visualizer needs to remember between frames."""
    def __init__(self):
        self.graph = Clases.Graph()
        self.start_node = None
        self.end_node = None
        self.mode = "NODE"
        self.next_char = 65

        self.first_selected = None
        self.second_selected = None
        self.awaiting_weight = False
        self.weight_input = ""

        self.animating = False
        self.visited_history = []
        self.animated_visited = []
        self.anim_index = 0
        self.current_eval = None
        self.step_timer = 0

        self.calc_path = []
        self.calc_weight = None
        self.final_path = []
        self.total_weight = None

    def clear(self):
        self.graph = Clases.Graph()
        self.start_node = None
        self.end_node = None
        self.next_char = 65
        self.first_selected = None
        self.animated_visited = []
        self.animating = False
        self.current_eval = None
        self.final_path = []
        self.total_weight = None


def create_buttons():
    buttons = []
    buttons.append(Button(10, 10, 80, 30, "Add Node", "NODE"))
    buttons.append(Button(100, 10, 80, 30, "Add Edge", "EDGE"))
    buttons.append(Button(190, 10, 80, 30, "Set Start", "START"))
    buttons.append(Button(280, 10, 80, 30, "Set End", "END"))
    buttons.append(Button(370, 10, 80, 30, "Run", "RUN"))
    buttons.append(Button(460, 10, 80, 30, "Clear", "CLEAR"))
    return buttons


def get_node_at(graph, pos):
    for node in graph.nodes:
        if np.hypot(node.x - pos[0], node.y - pos[1]) <= NODE_RADIUS:
            return node
    return None


def edge_in_path(edge, path):
    for i in range(len(path) - 1):
        if edge.first_node in (path[i], path[i + 1]) and edge.second_node in (path[i], path[i + 1]):
            return True
    return False


def start_animation(state):
    """Runs Dijkstra and prepares the step by step animation."""
    state.calc_weight, state.calc_path, state.visited_history = Clases.dijkstra(
        state.graph, state.start_node, state.end_node
    )
    state.final_path = []
    state.total_weight = None
    state.animated_visited = []
    state.anim_index = 0
    state.step_timer = STEP_DELAY
    state.current_eval = None
    state.animating = True


def update_animation(state, dt):
    if not state.animating:
        return

    state.step_timer += dt
    if state.step_timer < STEP_DELAY:
        return
    state.step_timer = 0

    if state.anim_index < len(state.visited_history):
        state.current_eval = state.visited_history[state.anim_index]
        state.animated_visited.append(state.current_eval)
        state.anim_index += 1
    else:
        state.animating = False
        state.current_eval = None
        state.final_path = state.calc_path
        state.total_weight = state.calc_weight


def handle_weight_key(state, event):
    """Reads the keyboard while the weight box is open."""
    if event.key == pygame.K_RETURN:
        if state.weight_input:
            try:
                weight = float(state.weight_input)
                state.graph.add_connection(state.first_selected, state.second_selected, weight)
            except ValueError:
                pass
        state.awaiting_weight = False
        state.first_selected = None
        state.second_selected = None
        state.weight_input = ""
    elif event.key == pygame.K_BACKSPACE:
        state.weight_input = state.weight_input[:-1]
    elif event.unicode.isdigit() or event.unicode == ".":
        state.weight_input += event.unicode


def handle_button_click(state, button):
    if button.mode == "RUN":
        if state.start_node and state.end_node:
            start_animation(state)
    elif button.mode == "CLEAR":
        state.clear()
    else:
        state.mode = button.mode
        state.first_selected = None


def handle_canvas_click(state, pos):
    node = get_node_at(state.graph, pos)

    if state.mode == "NODE":
        if not node:
            state.graph.add_node(chr(state.next_char), pos[0], pos[1])
            state.next_char = 65 + (state.next_char - 64) % 26

    elif state.mode == "EDGE":
        if node:
            if state.first_selected is None:
                state.first_selected = node
            elif state.first_selected != node:
                state.second_selected = node
                state.awaiting_weight = True
                state.weight_input = ""

    elif state.mode == "START":
        if node:
            state.start_node = node

    elif state.mode == "END":
        if node:
            state.end_node = node


def handle_click(state, buttons, pos):
    for button in buttons:
        if button.rect.collidepoint(pos):
            handle_button_click(state, button)
            return

    if pos[1] < TOOLBAR_HEIGHT:
        return

    handle_canvas_click(state, pos)


def handle_events(state, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state.awaiting_weight:
            if event.type == pygame.KEYDOWN:
                handle_weight_key(state, event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_click(state, buttons, event.pos)


def get_node_color(state, node):
    if node is state.current_eval:
        return YELLOW
    if node in state.final_path:
        return CYAN
    if node is state.start_node:
        return GREEN
    if node is state.end_node:
        return RED
    if node in state.animated_visited:
        return GRAY
    return WHITE


def get_cost_text(state, node):
    hidden = state.animating and node not in state.animated_visited and node is not state.start_node
    if node.path_cost == np.inf or hidden:
        return "inf"
    return str(node.path_cost)


def draw_edges(screen, font, state):
    for edge in state.graph.connections:
        p1 = (edge.first_node.x, edge.first_node.y)
        p2 = (edge.second_node.x, edge.second_node.y)

        if edge_in_path(edge, state.final_path):
            pygame.draw.line(screen, CYAN, p1, p2, 4)
        else:
            pygame.draw.line(screen, BLACK, p1, p2, 1)

        mid_x = (p1[0] + p2[0]) // 2
        mid_y = (p1[1] + p2[1]) // 2
        label = font.render(str(edge.weight), True, BLACK)
        screen.blit(label, (mid_x, mid_y))


def draw_nodes(screen, font, state):
    for node in state.graph.nodes:
        color = get_node_color(state, node)
        pygame.draw.circle(screen, color, (node.x, node.y), NODE_RADIUS)
        pygame.draw.circle(screen, BLACK, (node.x, node.y), NODE_RADIUS, 2)

        name_label = font.render(node.name, True, BLACK)
        screen.blit(name_label, (node.x - 5, node.y - 8))

        cost_label = font.render(f"c:{get_cost_text(state, node)}", True, BLACK)
        screen.blit(cost_label, (node.x - 15, node.y + 22))


def draw_weight_box(screen, font, state):
    pygame.draw.rect(screen, WHITE, (300, 250, 300, 70))
    pygame.draw.rect(screen, BLACK, (300, 250, 300, 70), 2)
    prompt = font.render("Enter Weight + Press Enter:", True, BLACK)
    typed = font.render(state.weight_input + "_", True, BLACK)
    screen.blit(prompt, (310, 260))
    screen.blit(typed, (310, 285))


def draw_result(screen, font, state):
    path_text = " -> ".join(node.name for node in state.final_path)
    result = font.render(f"Path: {path_text} | Weight: {state.total_weight}", True, BLACK)
    screen.blit(result, (10, 570))


def draw(screen, font, state, buttons):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, TOOLBAR_HEIGHT), (WINDOW_WIDTH, TOOLBAR_HEIGHT), 2)

    draw_edges(screen, font, state)
    draw_nodes(screen, font, state)

    for button in buttons:
        button.draw(screen, font, state.mode)

    if state.awaiting_weight:
        draw_weight_box(screen, font, state)

    if state.final_path:
        draw_result(screen, font, state)

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Dijkstra")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 15)

    state = AppState()
    buttons = create_buttons()

    while True:
        dt = clock.tick(30)
        update_animation(state, dt)
        handle_events(state, buttons)
        draw(screen, font, state, buttons)


if __name__ == "__main__":
    main()