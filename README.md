# Next-Read

Your personal book concierge for discovering your next page turner.

## Description

I love reading and books I can talk about books for hours. When I closer to finishing a book, I always wonder **'What Should I Read Next'**?

I made use of Anthropic's model to create 'Next Read': An intelligent book recommendation application designed to help you, my dear reader, find your perfect next book. Next Read analyzes your reading preferences, favorite genres, and past reads to suggest books that you're likely to love.

## Application Link

You can access the application at: https://nextread.streamlit.app/

A big thanks to Streamlit Community for providing home to Next Read

### Key Features:

- **Personalized Recommendations**: Get tailored book suggestions based on your reading history and preferences.
- **Genre Exploration**: Discover new books across various genres and styles.
- **AI-Powered Insights**: Benefit from advanced natural language processing to match you with books that align with your interests.
- **User-Friendly Interface**: Easy-to-use platform for seamless book discovery.
- **Detailed Book Information**: Access short and sweet details about recommended books, including summaries, author information, and reader reviews.

Whether you're a voracious reader looking for your next page-turner or someone trying to rekindle their love for reading, Next Read is your go-to companion for literary exploration.

## How It Works

Next Read uses the Anthropic API to analyze your inputs and generate personalized book recommendations. You provide a brief description of the book you wanna read next, like "A thriller set in a church" or "A murder mystery set in abookstore", optionally provide a book you have read in the genre which will enhance the recommendation provided. 

## Getting Started

### To install 

1. Clone the GitHub repository
2. Set up API Key on Antropic AI's portal (https://console.anthropic.com/settings/keys)
3. This application is deployed on Streamlit and uses secrets in Streamlit Cloud to secure the API Key. While running locally, replace st.secrets['API_KEY'] with os.environ['API_KEY']. 
4. Supplement your Anthropic API Key using terminal and depending on Windows/Linux/macOS, follow the instructions provided here (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) to provide api key as an environment variable 
5. Run your app by running: streamlit run app.py
6. Enjoy the recommendations

## Contributing

You are most welcome contributions to Next Read! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

Start your next reading adventure with Next Read – where every book is a new world waiting to be explored!