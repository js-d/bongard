import streamlit as st
import os


def display_images(problem_number):
    # Create two main columns for left and right images
    left_col, sep, right_col = st.columns([1, 0.1, 1])  # Adjust columns to add a separation

    # Add titles to each column
    left_col.markdown("### Left Images")
    right_col.markdown("### Right Images")

    # Create two subcolumns in each main column
    left_subcol1, left_subcol2 = left_col.columns(2)
    right_subcol1, right_subcol2 = right_col.columns(2)

    # Assign images to subcolumns in a zigzag pattern for both sides
    left_subcolumns = [
        left_subcol1,
        left_subcol2,
        left_subcol1,
        left_subcol2,
        left_subcol1,
        left_subcol2,
    ]
    right_subcolumns = [
        right_subcol1,
        right_subcol2,
        right_subcol1,
        right_subcol2,
        right_subcol1,
        right_subcol2,
    ]

    # Display images in the left subcolumns
    for i in range(1, 7):
        left_image_path = f"problems/{problem_number}/left_image_{i}.png"
        with open(left_image_path, "rb") as file:
            left_image_data = file.read()
            left_subcolumns[(i-1) % 2].image(
                left_image_data, caption=f"Left Image {i}", use_column_width=True
            )

    # Display images in the right subcolumns
    for i in range(1, 7):
        right_image_path = f"problems/{problem_number}/right_image_{i}.png"
        with open(right_image_path, "rb") as file:
            right_image_data = file.read()
            right_subcolumns[(i-1) % 2].image(
                right_image_data, caption=f"Right Image {i}", use_column_width=True
            )

def get_full_prompt():
    with open("prompt.txt", "r") as file:
            main_prompt = file.read()
    full_prompt = "What follows is a Bongard problem.\n"
    full_prompt += f"The following 6 images form the 'left' group.\n"
    full_prompt += "[left images]\n\n"
    full_prompt += f"The following 6 images form the 'right' group.\n"
    full_prompt += "[right images]\n\n"
    full_prompt += main_prompt
    return full_prompt




def load_model_response(problem_number, model_name):
    try:
        with open(f"problems/{problem_number}/{model_name}/response.txt", "r") as file:
            response_text = file.read()
            return response_text
    except FileNotFoundError:
        return "Model response not found"


def load_solution(problem_number):
    try:
        with open(f"problems/{problem_number}/solution.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Solution not found."


def main():
    st.title("Bongard Problem Solutions")

    # Input for problem number, constrained between 2 and 100
    problem_number = st.number_input(
        "Enter problem number", min_value=2, max_value=100, value=2, step=1
    )

    # Display the left and right images
    display_images(problem_number)

    # Display the solution
    solution = load_solution(problem_number)
    st.markdown("### Solution")
    st.markdown(solution)

    # Dropdown to select the model
    st.markdown("### Model")
    model_list = ["claude-3-haiku-20240307", "claude-3-opus-20240229"]
    model_name = st.selectbox("Select a model", model_list)

    # Display the model response (and prompt optionally)
    response = load_model_response(problem_number, model_name)
    st.markdown("### Model Response")
    
    show_prompt = st.checkbox("Show prompt for model response")
    if show_prompt:
        prompt = get_full_prompt()
        st.text_area("Prompt:", prompt, height=150)
 
    st.text_area("Response:", response, height=200)


if __name__ == "__main__":
    main()
