import streamlit as st
from chatbot import ComicChatbot

# Define the template for the chatbot responses

chatbot=ComicChatbot()


st.image("/Users/mazin/Desktop/05-avengers-5bcdaa762d680__880.jpg")
st.title("Comic Chatbot")
st.write("Welcome to Comic Chatbot! Type your questions about Marvel & DC comics.")

if "memory" not in st.session_state:
    st.session_state.memory = ""
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "latest_response" not in st.session_state:
    st.session_state.latest_response = ""

user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        if user_input.lower() == "sayanaro":
            st.write("Goodbye! See you next time.")
            

        # Get the chatbot response
        response = chatbot.get_response(st.session_state.memory, user_input)
        
        # Update latest response
        st.session_state.latest_response = response

        # Update memory
        st.session_state.memory += f"\nUser: {user_input}\nBot: {response}"
        
        # Update conversation history
        st.session_state.conversation.append({"user": user_input, "bot": response})

        # Clear the input
        st.session_state.user_input = ""

# Display the latest bot response
if st.session_state.latest_response:
    st.write("### Latest Bot Response")
    st.write(f"**Bot**: {st.session_state.latest_response}")

# Display conversation history in an expandable section
with st.expander("Conversation History"):
    for chat in st.session_state.conversation:
        st.write(f"**You**: {chat['user']}")
        st.write(f"**Bot**: {chat['bot']}")


