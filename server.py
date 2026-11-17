''' This function initiates the application of emotion detection to be 
    executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' Receives the text from the HTML interface and runs the emotion detector()
        in the emotion detection  function. The output returned shows the emotiona
        and its score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")
    # Pass the text to the emotion_detector function and store the response
    emotions = emotion_detector(text_to_analyze)
    # Convert the dictionary to a list of (key,value) pair turple
    emotions_list = list(emotions.items())
    # Call the response_to_string function with the emotions_list as agrument
    response = response_to_string(emotions_list)
    # Return the output with the requested format
    return response

def response_to_string(list_1):
    """ Convert the given list to string ouput
    """
    # output string to be returned
    output = "For the given statment, the system response is "
    # length of the given list
    list_len = len(list_1)
    # Convert the list to string eith the required format
    for i in range(list_len):
        if i <= list_len - 4:
            output += (f"'{list_1[i][0]}': {list_1[i][1]}, ")
        elif i == list_len - 3:
            output += (f"'{list_1[i][0]}': {list_1[i][1]} and ")
        elif i == list_len - 2:
            output += (f"'{list_1[i][0]}': {list_1[i][1]}. ")
        elif i == list_len - 1:
            output += (f"The dominant emotion is {list_1[i][1].split()[0]}.")
    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

# Executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
