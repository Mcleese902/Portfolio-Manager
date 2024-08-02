from anticaptchaofficial.imagecaptcha import imagecaptcha

def solve_captcha(api_key, image_path):
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(api_key)
    
    captcha_text = solver.solve_and_return_solution(image_path)
    if captcha_text != 0:
        print("captcha text " + captcha_text)
        return captcha_text
    else:
        print("task finished with error " + solver.error_code)
        return None
