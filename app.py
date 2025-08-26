import pickle
import streamlit as st
import requests
import pyttsx3
import speech_recognition as sr
import ast

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=68f44c972e9163ee458e1b708c5dabfa".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:11]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names,recommended_movie_posters
    except:
        return -1,-1


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()
    
def SpeechRecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            text_to_speech('searching for' + text)
            return text
        except:
            text_to_speech("couldn't able to recognize your voice")
            return -1
    

def Show_Recommendation(movie):
    recommended_movie_names, recommended_movie_posters = recommend(movie)  
    try:

            col1, col2, col3, col4, col5= st.columns(5)
            with col1:
                    
                st.image(recommended_movie_posters[0])
                st.text(recommended_movie_names[0])
            with col2:
                    
                st.image(recommended_movie_posters[1])
                st.text(recommended_movie_names[1])

            with col3:
                    
                st.image(recommended_movie_posters[2])
                st.text(recommended_movie_names[2])
            with col4:
                    
                st.image(recommended_movie_posters[3])
                st.text(recommended_movie_names[3])
            with col5:
                    
                st.image(recommended_movie_posters[4])
                st.text(recommended_movie_names[4])
                
                
            col6, col7, col8, col9, col10= st.columns(5)
            with col6:
                    
                st.image(recommended_movie_posters[5])
                st.text(recommended_movie_names[5])
            with col7:
                    
                st.image(recommended_movie_posters[6])
                st.text(recommended_movie_names[6])
            with col8:
                    
                st.image(recommended_movie_posters[7])
                st.text(recommended_movie_names[7])
            with col9:
                
                st.image(recommended_movie_posters[8])
                st.text(recommended_movie_names[8])
            with col10:
                    
                st.image(recommended_movie_posters[9])
                st.text(recommended_movie_names[9])
            return recommended_movie_names
            
    except:
        st.write("NO SUCH MOVIE IN DATABASE ....... SEARCH FOR ANOTHER ONE.....")
        text_to_speech("NO SUCH MOVIE IN DATABASE")
        return -1

def design(image,name):

    col1, col2, col3, col4, col5= st.columns(5)
    with col1:             
        st.image(fetch_poster(image[0]))
        st.text(name[0])
    with col2:
                    
        st.image(fetch_poster(image[1]))
        st.text(name[1])

    with col3:
                    
        st.image(fetch_poster(image[2]))
        st.text(name[2])
    with col4:
                    
        st.image(fetch_poster(image[3]))
        st.text(name[3])
    with col5:
                
        st.image(fetch_poster(image[4]))
        st.text(name[4])
                
                
    col6, col7, col8, col9, col10= st.columns(5)
        
    with col6:            
        st.image(fetch_poster(image[5]))
        st.text(name[5])
    with col7:
                    
        st.image(fetch_poster(image[6]))
        st.text(name[6])
    with col8:
                    
        st.image(fetch_poster(image[7]))
        st.text(name[7])
    with col9:
                
        st.image(fetch_poster(image[8]))
        st.text(name[8])
    with col10:
                    
        st.image(fetch_poster(image[9]))
        st.text(name[9])
    

st.header('Movie Recommender System')
movies = pickle.load(open('D:\\collage stuff\\Main Project\\MovieRecommenderSystem\\movie_list.pkl','rb'))
similarity = pickle.load(open('D:\\collage stuff\\Main Project\\MovieRecommenderSystem\\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)
if st.button('voice input'):
    selected_movie = SpeechRecognition()
    if selected_movie != -1:
        recommended_movie_names = Show_Recommendation(selected_movie)
        if recommended_movie_names == -1:   
            text_to_speech('SEARCH FOR ANOTHER ONE')
        else:
            for i in range(0,5):
                text_to_speech(recommended_movie_names[i])
    

if st.button('Show Recommendation'):
    
    recommended_movie_names = Show_Recommendation(selected_movie)
    if recommended_movie_names == -1:   
        text_to_speech('SEARCH FOR ANOTHER ONE')
    else:   
        for i in range(0,5):
            text_to_speech(recommended_movie_names[i])
            
            

genres = ['Action', 'Science Fiction', 'Fantasy', 'Thriller', 'Romance']
fp = open("genres.txt")

for i in range(0,5):
    name = []
    image = []  
    st.text(genres[i])
    for j in range(0,10): 
        lines = fp.readline()
        my_list = ast.literal_eval(lines)
        name.append(my_list[0])
        image.append(my_list[1])
    design(image,name)


