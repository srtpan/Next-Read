#import libraries
import streamlit as st
import anthropic
import os
import time

#title of the application
st.header("📖 Next Read")
st.subheader("Find your next favourite book here")

#function to call the anthropic API, get response for the question submitted
def anthropic_output(question):
    #keep the API Key secure using secrets inside streamlit cloud
    os.environ['API_KEY'] == st.secrets['API_KEY']
    client = anthropic.Anthropic(
        api_key= st.secrets["API_KEY"]
    )

    #properties stored within Anthropic API
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        #provide system prompt here
        system="You are the owner of a big bookstore in London and love to recommend books to users. They tell you what kind of books they like, optionally give you one or two books that they liked, and then request to suggest 5-6 books. You reply in a calm, mature, and friendly way, by providing a little about what you think of the book they gave as an example and then provide a recommendation in the format of a list containing the book name: provide a friendly introduction about the book and what you liked about it in one sentence. You are educated and speak in simple language, with no overused words like delighted, resonate, etc. ",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return message.content[0]


#create a form that people can submit to generate response from the app
with st.form("my_form"):
    st.subheader("Describe the kind of book you want to read...")
    pt1 = st.text_input("e.g. A cozy mystery set in London, A historical fiction based in India, etc."
    )
    pt2 = st.text_input(
    "Optional: Do you have any similar book in mind?"
    )

    submitted = st.form_submit_button("Submit")
    #this works only when 'submit' button is entered
    if submitted:
        progress_text = "Searching the library for you..."
        my_bar = st.progress(0, text=progress_text)
        #a progress bar for the users
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        #since part 2 of the text response is optional, adding a check
        if pt2=="":
            text_response= anthropic_output(f"Hi, I love {pt1}, can you please recommend me some books?")
            st.markdown(text_response.text)
            time.sleep(1)
            my_bar.empty()
        
        #if the optional details are entered
        elif pt2!="":
            text_response= anthropic_output(f"Hi, I love {pt1}, and loved the book {pt2} can you please recommend me some books?")
            st.markdown(text_response.text)
            time.sleep(1)
            my_bar.empty()

        #if nothing entered then this is displayed
        else:
            st.markdown("Please enter the input fields")
