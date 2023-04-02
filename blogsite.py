import streamlit as st

# Create a dictionary to store blog posts
blog_posts = {}

# Define a function to create a new blog post
def create_post(title, content, media):
    global blog_posts
    blog_posts[title] = {"content": content, "media": media}
	
    for title in blog_posts:
        st.write(f"## {title}")
        st.write(blog_posts[title]["content"])
        media = blog_posts[title]["media"]
        if media is not None:
            st.image(media)
        st.write("---")

# Define the Streamlit app
def app():
    # Add a title to the app
    st.title("Blog Site")

    # Create a sidebar menu with options to create a new blog post or view all blog posts
    menu = ["Create Blog", ""]
    choice = st.sidebar.selectbox("Select an option", menu)

    # If the user chooses to create a new blog post, show a form to create the post
    if choice == "Create Blog":
        st.subheader("Create a New Blog Post")
        # Get the title, content, and media for the new post
        title = st.text_input("Title")
        content = st.text_area("Content")
        media = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png"])

        # When the user clicks the "Create" button, add the post to the dictionary
        if st.button("Create"):
            create_post(title, content, media)
            st.success("Blog post created!")
            st.balloons()

# Run the app
if __name__ == "__main__":
    app()
