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
    response = emotion_detector(text_to_analyze)

    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

# Executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
