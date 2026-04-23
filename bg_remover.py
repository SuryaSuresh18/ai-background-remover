from rembg import remove
from PIL import Image
import io

class BackgroundRemover:
    """
    Singleton class to ensure the ML model
    is initialized only once.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BackgroundRemover, cls).__new__(cls)
        return cls._instance

    def remove_background(self, image_bytes: bytes) -> bytes:
        """
        Removes background and returns PNG bytes with transparency.
        """
        try:
            input_image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
            output_image = remove(input_image)

            output_buffer = io.BytesIO()
            output_image.save(output_buffer, format="PNG")
            return output_buffer.getvalue()

        except Exception as e:
            raise RuntimeError(f"Background removal failed: {str(e)}")