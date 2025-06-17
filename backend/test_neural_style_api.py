import requests

# Set the URL of the neural style imitation endpoint
url = "http://127.0.0.1:8000/api/neural_style_imitate"

# Open content and style images to simulate the POST request
content_image = {'content_image': open('/home/cj2k4211/formforge/images/content_image.jpg', 'rb')}
style_image = {'style_image': open('/home/cj2k4211/formforge/images/style_image.jpg', 'rb')}

# Send the POST request with the images
response = requests.post(url, files={**content_image, **style_image})

# Print the response from the API
print(response.json())

# Close the files
content_image['content_image'].close()
style_image['style_image'].close()
