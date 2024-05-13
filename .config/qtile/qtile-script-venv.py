from rule34Py import rule34Py
import os, requests, logging

logging.basicConfig(
    filename="scriptvenv.log",  # File name for logs
    level=logging.DEBUG,    # Minimum severity level to log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Format for log messages
)

def download_image(url, file_path, file_name):
    """Downloads an image from the specified URL and saves it to disk.

    Args:
      url: The URL of the image to download.
      file_path: The directory path where the image should be saved.
      file_name: The desired filename for the downloaded image.
    """

    # Create the full path for the image
    full_path = os.path.join(file_path, file_name)

    # Send a GET request to the image URL
    response = requests.get(url, stream=True)

    # Check for successful response status code (usually 200)
    response.raise_for_status()

    # Open the file in binary write mode
    with open(full_path, "wb") as file:
        for chunk in response.iter_content(1024):
        # Write the downloaded data chunk by chunk to the file
           file.write(chunk)
    logging.debug("Downloaded an image")

def random_r34_img():
    r34py = rule34Py()
    random = r34py.random_post(["-loli", "-ai_generated", "-furry"])    
    logging.debug(random.size)
    if random.content_type == "image":
        logging.debug("Found an image")
        logging.debug(random.tags)
        logging.debug(random.image)
        return random.image
    logging.debug("Not an image")

image = random_r34_img()

download_image(image, "./.config/qtile", "test.png")
