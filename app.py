import requests
import streamlit as st

ran_once = False

st.set_page_config(page_title="Time Complexity Calculator")


# function call 
def get_response(message_txt): 

    global ran_once
    if(ran_once == True): 
        return
       
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": message_txt + "   what is the time complexity of the code." + " Answer format should strictly be the following" + "      Time compleity: O() . then next line" + " Explanation: • <1st very short bullet point>. • <2nd very short bullet point>. • <3rd very short bullet point>."
            }
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }
    headers = {
    	"content-type": "application/json",
        "X-RapidAPI-Key": "d8c5b8fa03mshbd1888360322149p1ecd06jsn52e68e92a7e3",
        "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
    }

    if(ran_once == True):
        return
    
    response = requests.post(url, json=payload, headers=headers)
    ran_once = True
    return (response.json()['result'])


    # Time Complexity: O(log n)

    # Explanation:

    # * The function uses recursion to calculate the product of all positive integers 
    # up to a given number n.
    # * Each recursive call reduces n by 1 and doubles the result, which takes logarithmic time to execute as the base is reduced with each call.
    # * As the size of input decreases, it becomes smaller at each level of recursion 
    # until it reaches 1, so the total runtime will increase logarithmically with the 
    # input.


def get_stuff_printed(result):

    big_O = result[ result.index("O") : result.index(")") + 1 ]

    if(big_O[ big_O.index("(") + 1 : big_O.index(")")] == "..."):
        return

    info2 = result[result.index("Explanation:") + len("Explanation:") : len(result)] 
    arr = info2.split("•")
    info = ""
    for i in range(1, len(arr)):
        info += "• " + arr[i] + "\n"

    st.metric(label="heuf", label_visibility="collapsed", value=big_O)
    st.info(info)


st.header("Time Complexity Calculator", anchor=False)

st.divider()

message_txt = st.text_area(
    label="ihrgir",
    label_visibility="collapsed",
    height=250,
    placeholder="Paste/Write Code ",
    )

st.divider()



result = get_response(message_txt=message_txt)

print(result)

get_stuff_printed(result)

# print("x\u00b2 + y\u00b2 = 2") # x² + y² = 2
