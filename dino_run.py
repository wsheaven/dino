from PIL import ImageGrab, ImageOps
import pyautogui 
import time
import numpy as np
import win32api, win32con 
import win32gui


class Bot:

    def __init__(self):
        self.dino_coords = (400, 675)  
        self.make_jump = 273
        self.area = (self.dino_coords [0] + 100, self.dino_coords[1],
                     self.dino_coords[0] + 160, self.dino_coords[1] + 5)

    def set_area(self, x1, x2):
        self.area = (self.dino_coords [0] + x1, self.dino_coords[1],
                        self.dino_coords[0] + x2, self.dino_coords[1] + 5)


    def vision_calculation(self, time_diff):
        """
        Change obstacle detection distance based on how long the game has been played. 
        """
        if time_diff > 130:
            print("eleven")
            self.set_area(770,830)

        elif time_diff > 120:
            print("nine")
            self.set_area(720,780)

        elif time_diff > 110:
            print("eight")
            self.set_area(730,790)
 
        elif time_diff > 105:
            print("seven") 
            self.set_area(650,710)

        elif time_diff > 90:
            print("six")
            self.set_area(600,660)

        elif time_diff > 75 :
            print("five") 
            self.set_area(530,590)

        elif time_diff > 60:
            print("four")
            self.set_area(400,460)

        elif time_diff > 50:
            print("Three")
            self.set_area(330,390)

        elif time_diff > 30:
            print("Two")
            self.set_area(250,310)

        else:
            print("One")
            self.set_area(130,190)

    def jump(self):
        """
        Jump over the obstacle.
        """
        pyautogui.keyUp('down')
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        pyautogui.keyDown('down')
        

    def detection_area(self):
        """
        Checks to see if any obstacles are incoming. 
        """
        image = ImageGrab.grab(self.area)
        gray_img = ImageOps.grayscale(image)
        arr = np.array(gray_img.getcolors())
        # print(arr.mean())
        return arr.mean()


    def night_check(self):
        """
        Check the colour value of a pixel in the sky. 
        """
        return win32gui.GetPixel(win32gui.GetDC(0), 400,525)

    def click(self,x,y):
        # Move the cursor to a position on the screen and click. 
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


    def main(self):
        """
        The main loop of the bot 
        """ 
        # Click the dino window to bring it to the front and start the game timer. 
        self.click(300,500)
        self.start_time = time.time()
        
        while True:
            # Check how long the game has been playing. 
            self.time2 = time.time()
            self.time_diff = self.time2 - self.start_time
            
            # If the game has switched over to night mode check different values for the obstacle avoidance. 
            if self.night_check() != 16777215:

                # Detect if there is an obstacle in front of the dinosour and if there is then jump.
                if self.detection_area() < 149.9: 
                    self.jump()
                    print("First jump")
                    self.vision_calculation(self.time_diff)
        
            # Detect if there is an obstacle in front of the dinosour and if there is then jump. 
            elif self.detection_area() < self.make_jump:

                self.jump()
                self.vision_calculation(self.time_diff)

            
            
 
      
# Initialize the bot class and start it by calling the "main" method.
bot  = Bot()
bot.main()

