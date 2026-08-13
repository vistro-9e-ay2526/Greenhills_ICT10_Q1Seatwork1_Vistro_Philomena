# String Formatting
from pyscript import display, document

MyName = 'Philomena Maria Isabel I. Vistro' #str
age = 14 #int
H3ight = 166.8 #float
Countries_Travel = ['Italy', 'Iceland', 'Japan'] #list
student_type = False #bool
AboutMe = {
    'color':'Blue', 
    'car_brand':'Toyota', 
    'shoe-size':'39', 
    'best_friend':'Bela'
} #dict
fruit_basket = set(['Caimito', 'Strawberry', 'Mango', 'Melon', 'Rambutan']) #set
days_7 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple


display(
    f'Hi there! I am {MyName}.'
    f'I am {age} years old and {H3ight} centimeters tall\n.', 
    target='seatwork 1')

display(
    f'Am I a new student in OBMC? {student_type}.', 
    target='seatwork 1')

display(
    f'Here are some things about me: {AboutMe}.'
    f'Countries I want to travel to include: {Countries_Travel}'
    f'and fruits I would like to take with me are {fruit_basket}.', 
    target='seatwork 1')

display(
    f'There are 7 days in a week. They are {days_7}.', target='seatwork 1')
