import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
from tools import seasons

template = """
    You are an AI travel agent.
    Your goal is :
    - Recommend the best holiday plans for the users that reach you.
    - The holiday plan that you recommend must fit in season of the year that the user gives you.

    For that, the users will give you:
    - A City.
    - The season of the year.

    Here are some examples of different cities:
    - Buenos Aires, Rome, Paris, New York, Ciudad de México, Montevideo, Tokyo, Osaka, Bangkok, Bali, Cape Town. 
    Here are some examples of different seasons:
    - Summer, Autumn, Winter, Spring.

    For the recommendation follow the next format:
    -Start the recommendation with a simple explaination of your choices.
    -5 one-line recommendations of plans to do in the city given in the season given.
    -The recommendations should look like this:
        1.
        2.
        3.
        4.
        5.
    -End with the recommendation of two other cities near in the same country.

    Below is the city and the season of the trip:
    CITY: {city}
    SEASON: {season}

    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["city", "season"],
    template=template,
)

llm = OpenAI(temperature=1, openai_api_key='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')

st.set_page_config(page_title="Holiday Planner", page_icon=":robot:")
st.header("Holiday Planner")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Are you looking for guidance on what to do and where to go? Our website provides the perfect solution. Simply enter the city you're planning to visit, along with the season of your stay, and we'll help you plan your itinerary. \n\n This tool \
                is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and made by \
                [@elthomate](https://twitter.com/elthomate). \n\n View Source Code on [Github](https://github.com/gkamradt/globalize-text-streamlit/blob/main/main.py)")

with col2:
    st.image(image="hiroshi_nagai.jpg", width=500, caption="Hiroshi Nagai ©")

st.markdown("## Let's plan your trip!")

def get_city():
    input_text = st.text_area(label="city Input", 
                                  label_visibility='collapsed', 
                                  placeholder="Where you want to go?", 
                                  key="city_input")
    return input_text

city_input = get_city()

season_input = st.selectbox(
        'When you want to go ...?',
        seasons)

if st.button('GO ✈️', use_container_width=True):

    final_prompt = prompt.format(city=city_input, season=season_input)

    formatted_trip = llm(final_prompt)

    st.markdown("## Here's your holiday!!")
    st.write(formatted_trip)