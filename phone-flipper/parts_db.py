parts = {

"iphone13":{

"screen":4200,
"battery":1800,
"camera":3500,
"camera_glass":800

},

"iphone12":{

"screen":3800,
"battery":1600,
"camera":3000,
"camera_glass":700

},

"iphone11":{

"screen":3200,
"battery":1500,
"camera":2800,
"camera_glass":600

}

}

def get_part(model,part):

    if model not in parts:
        return None

    return parts[model].get(part)