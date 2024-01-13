import streamlit as st
import pickle

st.set_page_config(page_title = 'Game Recommender', page_icon='🎮')

games = pickle.load(open("games_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
games_list = games['Title'].values
st.header("Game Recommender! 🎲")
st.write("Level up your gaming experience! This game recommender will help you find your next favorite game based on your previous play.")
selectvalue = st.selectbox("Select Game", games_list)

def remove(string):
    return string.replace(" ", "")

def recommend(game):
    index = games[games['Title']==game].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    list_of_games = []
    for i in distance[3:12]:
        check = games.iloc[i[0]].Title
        if check not in list_of_games:
            list_of_games.append(check)
    return list_of_games


def recommend_summary(game):
    index = games[games['Title']==game].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    list_of_games_summary = []
    for i in distance[3:12]:
        check = games.iloc[i[0]].tags
        if check not in list_of_games_summary:
            list_of_games_summary.append(check)
    return list_of_games_summary


if st.button("Find Similar Games"):
    game_name = recommend(selectvalue)
    game_summary = recommend_summary(selectvalue)
    for i in range(0, len(game_name)):
        yo = f'https://www.google.com/search?q={remove(game_name[i])}'
        summary_split = game_summary[i].rsplit('[', 1)
        actual_summary = summary_split[0]
        genres = summary_split[1][0:-1]
        st.text(f"{i+1}. {game_name[i]}")
        st.write({genres})
        st.write(actual_summary)
        st.write(f'[Check out this game!]({yo})')
   
    
    