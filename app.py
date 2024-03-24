import streamlit as st
from streamlit_carousel import carousel

from api_keys import gemini_key, openai_key


# Function to check if a given string is empty or not
def is_not_blank(string):
    return bool(string and not string.isspace())


# Function to display the warning sign to user if the required fields are not filled
def display_warning_msg():
    st.sidebar.warning("Please fill in the required fields", icon="⚠️")


# Function to display the generated blog content
def display_content(images):
    carousel(items=images, width=0.5)


# Main function
def main():

    blog_images = [
        dict(
            title="",
            text="A distant mountain chain preceded by a sea",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        ),
    ]

    # Change the default layout of the app
    st.set_page_config(layout="wide")

    # Add title and sub header for the app
    st.title("✨✍️ AI Blog Assistant")
    st.subheader("Now create blog using AI", divider="rainbow")

    # Adding sidebar to the app
    with st.sidebar:
        st.title("Blog details")

        # Blog title as input from the user
        blog_title = st.text_input("Blog title: ")

        # Blog keywords to create the blog
        blog_keywords = st.text_area("Blog keywords (comma-sperated value): ")

        # Number of words for the blog
        blog_num_size = st.number_input(
            "Blog length: ", min_value=200, max_value=1000, step=50
        )

        # Number of images to generate for the blog
        blog_num_size = st.number_input("Number of images: ", min_value=1, max_value=10)

        button = st.button("Generate")

    # Display default "No blog" text when the app is started
    no_image = st.image("images/no_image.png")
    no_image_caption = st.caption("No blogs generated")

    # Main content area
    if button:
        if is_not_blank(blog_title) and is_not_blank(blog_keywords):
            no_image.empty()
            no_image_caption.empty()
            display_content(blog_images)
        else:
            # Display warning if the required fields are not filled
            display_warning_msg()


if __name__ == "__main__":
    main()
