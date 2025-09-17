import streamlit as st
import random
import time

# Initialize game state
if 'snake' not in st.session_state:
    st.session_state.snake = [(10, 10)]
    st.session_state.food = (5, 5)
    st.session_state.direction = 'RIGHT'
    st.session_state.score = 0
    st.session_state.game_over = False

GRID_SIZE = 20
CELL_SIZE = 20

def move_snake():
    head = st.session_state.snake[0]
    
    if st.session_state.direction == 'UP':
        new_head = (head[0], head[1] - 1)
    elif st.session_state.direction == 'DOWN':
        new_head = (head[0], head[1] + 1)
    elif st.session_state.direction == 'LEFT':
        new_head = (head[0] - 1, head[1])
    else:  # RIGHT
        new_head = (head[0] + 1, head[1])
    
    # Check boundaries
    if (new_head[0] < 0 or new_head[0] >= GRID_SIZE or 
        new_head[1] < 0 or new_head[1] >= GRID_SIZE or
        new_head in st.session_state.snake):
        st.session_state.game_over = True
        return
    
    st.session_state.snake.insert(0, new_head)
    
    # Check food
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    else:
        st.session_state.snake.pop()

def draw_game():
    grid = [['⬜' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Draw snake
    for segment in st.session_state.snake:
        grid[segment[1]][segment[0]] = '🟢'
    
    # Draw head
    head = st.session_state.snake[0]
    grid[head[1]][head[0]] = '🔴'
    
    # Draw food
    food = st.session_state.food
    grid[food[1]][food[0]] = '🍎'
    
    return '\n'.join([''.join(row) for row in grid])

st.title("🐍 Snake Game")
st.write(f"Score: {st.session_state.score}")

# Controls
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("⬆️") and st.session_state.direction != 'DOWN':
        st.session_state.direction = 'UP'
with col2:
    if st.button("⬇️") and st.session_state.direction != 'UP':
        st.session_state.direction = 'DOWN'
with col3:
    if st.button("⬅️") and st.session_state.direction != 'RIGHT':
        st.session_state.direction = 'LEFT'
with col4:
    if st.button("➡️") and st.session_state.direction != 'LEFT':
        st.session_state.direction = 'RIGHT'
with col5:
    if st.button("🔄 Reset"):
        st.session_state.snake = [(10, 10)]
        st.session_state.food = (5, 5)
        st.session_state.direction = 'RIGHT'
        st.session_state.score = 0
        st.session_state.game_over = False

# Game logic
if not st.session_state.game_over:
    move_snake()
    st.text(draw_game())
    time.sleep(0.1)
    st.rerun()
else:
    st.error("Game Over! Click Reset to play again.")
    st.text(draw_game())