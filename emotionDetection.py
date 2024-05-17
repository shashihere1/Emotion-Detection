from pysentimiento import create_analyzer

# Defining the emotion detection function
def emotionDetection(text):
    # Create an emotion analyzer
    emotion = create_analyzer(task='emotion', lang='en')
    # Predict the emotion of the input text
    result = emotion.predict(text)
    # Return the detected emotion
    return result.output

# Example usage
print(emotionDetection("I am happy"))  # Output: joy
