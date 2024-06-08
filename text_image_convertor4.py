from PIL import Image, ImageDraw, ImageFont

def background_gradient_convertor( width , height , start_color , end_color ):
    img = Image.new( 'RGB' , ( width,height) , start_color)
    draw = ImageDraw.Draw(img)

    #this thing converts the two colors into one or mixings the rwo colors
    for i in range(height):
        r = start_color[0] + ( end_color[0] -start_color[0] ) * i // height
        g = start_color[1] + ( end_color[1] - start_color[1] ) * i // height
        b = start_color[2] + ( end_color[2] - start_color[2] ) * i // height
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    return img



def text_to_image( font_style , output_path , text ):
    width , height = 800, 400

    # slecting the gradient colors

    start_color = (255, 192, 203) #its a light pink color
    end_color = (128, 0, 128) #its a light purple color
    img = background_gradient_convertor( width , height , start_color , end_color)

    #initializing the ImageDraw
    d = ImageDraw.Draw(img)

    #setting the font..
    try:
        font = ImageFont.truetype(font_style,40)
    except IOError:
        font = ImageFont.load_default()

    # Get text bounding box
    text_bbox = d.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw text on image
    text_color = (255, 255, 255)  # white text
    d.text((x, y), text, fill=text_color, font=font)

    # Save the image
    img.save(output_path)

    return output_path