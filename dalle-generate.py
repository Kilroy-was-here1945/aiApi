import os
import openai
import base64
import time
import simplejson as json

def generate_image_html_with_url(folder_path):
        """
        Given a folder path, generates a string containing HTML image elements
        with the path to the images included in the string.

        Args:
            folder_path (str): The path to the folder containing the image files.

        Returns:
            str: The string containing HTML image elements with the path to the images.
        """
        image_html = ""

        # Loop through all the files in the folder
        for file_name in os.listdir(folder_path):
            # Check if the file is an image file
            if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
                # Generate the HTML image element for the file
                image_html += f"<img src='{os.path.join(folder_path, file_name)}'>"

        return image_html

def dalleUrl(prompt):
    openai.api_key = "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"

    # print(openai.api_key)

    res = openai.Image.create(
        prompt=""+prompt+"",
        n=1,
        size="1024x1024"
    )
    # res = res.decode()
    # json_obj = json.loads(res)

    # url = json_obj['data'][0]['url']

    # print(url)
    res = res["data"][0]["url"]


    return res

def dalleUrlSavedToComp(prompt, amount, resolution):
    openai.api_key = "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"

    # print(openai.api_key)

    res = openai.Image.create(
        prompt=""+prompt+"",
        n=amount,
        size=resolution,
        response_format="b64_json"
    )
    for i in range(0,len(res['data'])):
        b64 = res['data'][i]['b64_json']
        filename = f'image_{int(time.time())}_{i}.png'
        print('Saving file ' + filename + '')
        with open(filename, 'wb') as f:
            f.write(base64.urlsafe_b64decode(b64))
    
    
    return res





# print(dalleUrlSavedToComp("6ft tall man and 5ft tall woman holding hands on the beach looking into the sunset", 1, "256x256"))
print(generate_image_html_with_url(dalleUrl("a cute puppy shooting a machine gun")))



# the below code is an attempt to bring the above code to a local server and feed the functions 
# above with text box inputs so it can create images 





# from flask import Flask, request, render_template
# import os
# import openai
# import base64
# import time

# app = Flask(__name__)

# def dalleUrl(prompt):
#     openai.api_key = "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"

#     res = openai.Image.create(
#         prompt=""+prompt+"",
#         n=1,
#         size="1024x1024"
#     )

#     return res


# def dalleUrlSavedToComp(prompt, amount, resolution):
#     openai.api_key = "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"

#     res = openai.Image.create(
#         prompt=""+prompt+"",
#         n=amount,
#         size=resolution,
#         response_format="b64_json"
#     )

#     for i in range(0,len(res['data'])):
#         b64 = res['data'][i]['b64_json']
#         filename = f'image_{int(time.time())}_{i}.png'
#         print('Saving file ' + filename + '')
#         with open(filename, 'wb') as f:
#             f.write(base64.urlsafe_b64decode(b64))

#     return res

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         amount = int(request.form['amount'])
#         resolution = request.form['resolution']
#         res = dalleUrlSavedToComp(prompt, amount, resolution)
#         return "Images generated and saved to disk."
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
