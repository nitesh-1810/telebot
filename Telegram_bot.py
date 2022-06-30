from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

print("Bot started....")
  
updater = Updater("5530494101:AAFhGyQpZtRvR_4aqWbZtew7sY9W9VaJwvk",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello Student, Welcome to the Exam Preparation Bot.Please write\
        /Programming_lang to see the Programming language resources\
        /DSA to see the Data Structure resources ")

def back(update: Update, context: CallbackContext):
    update.message.reply_text("Please write \n"+"\
/Programming_lang to see the Programming language resources\
 /DSA to see the Data Structure resources ")
  
def Programming_lang(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Resources :-
    /Codecademy - Codecademy is possibly one of the most popular online code-teaching websites. At Codecademy, you can learn seven different languages: HTML, CSS, Javascript, jQuery, Python, Ruby, and PHP. Once you learn the basic languages, you can move on to more advanced tasks like building a website, making a Rails app, using APIs to make applications, and other fun goals.\n"""+"""
    /Khan_Academy - Khan Academy started as one man tutoring his cousin. Today, Khan Academy teaches people all over the world. Unlike other online resources to teach coding, Khan Academy isn’t limited to just computing courses—you can also learn about various subjects from math to arts & humanities. Under Khan Academy’s computing courses, you can learn JavaScript, HTML, and CSS. You can also learn computer science basics. If you only have a short amount of time, there is even an “Hour of Code” option\n"""+"""
    /Coursera - If you like the style of university courses but don’t want to pay the university price, websites like Coursera and edX have compiled multiple different computer science courses that you can take from top schools all over the world. Courses are constantly changing, so if the language you want to learn isn’t currently being taught, you may find a course on it at a later date.\n"""+"""
    /w3schools - If you want to learn how to build a website, apps, or games, Code Avengers is the site for you. Code Avengers has over 100 hours of courses teaching you how to build websites in HTML & CSS and games or apps in JavaScript. Before you even sign up, you can try out the lower level lessons. To help you remember what you learned, you can take notes along the way which will save to your account.\n"""+"""
    /back - Return to main menu""")
def DSA(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Resources :-
    /leetcode - LeetCode is the best platform to help you enhance your skills, expand your knowledge and prepare for technical interviews. LeetCode provides problems for a variety of programming languages. This platform is best when preparing for technical interviews and sharpening your data structures and algorithms.\n"""+"""
    /freeCodeCamp - Freecodecamp is one of the best online platforms to learn to program freely. Their curriculum is very sequential and beginner-friendly. Their algorithm and data structures curriculum is one of the best in taking you through programming basics.\n"""+"""
    /Coderbyte - Coderbyte is a platform for preparing for both technical and non-technical programming interviews. Many companies use Coderbyte to access developers on various topics concerning their relevant positions.\n"""+"""
    /AlgoExpert - AlgoExpert is also one of the best platforms for learning algorithms and data structures. Their problems are essential in providing beginner-friendly problems for beginners and experts on various topics concerning computer science.\n"""+"""
    /back - Return to main menu""")
  
  
def Codecademy_url(update: Update, context: CallbackContext):
    update.message.reply_text("Codecademy Link =>\
    https://www.codecademy.com/")
  
  
def Khan_Academy_url(update: Update, context: CallbackContext):
    update.message.reply_text("khanacademy Link =>\
    https://www.khanacademy.org/computing/computer-programming")
  
  
def Coursera_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Coursera URL => \
        https://www.coursera.org/in")
  
  
def w3schools_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "w3schools URL => https://www.w3schools.com/")

def leetcode_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "leetcode Link =>\
         https://leetcode.com/")
  
  
def freeCodeCamp_url(update: Update, context: CallbackContext):
    update.message.reply_text("freeCodeCamp Link =>\
    https://www.freecodecamp.org/")
  
  
def Coderbyte_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Coderbyte URL => \
        https://coderbyte.com/")
  
  
def AlgoExpert_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "AlgoExpert URL => https://www.algoexpert.io/product")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('back', back))
updater.dispatcher.add_handler(CommandHandler('Programming_lang', Programming_lang))
updater.dispatcher.add_handler(CommandHandler('DSA', DSA))
updater.dispatcher.add_handler(CommandHandler('Khan_Academy', Khan_Academy_url))
updater.dispatcher.add_handler(CommandHandler('Coursera', Coursera_url))
updater.dispatcher.add_handler(CommandHandler('w3schools', w3schools_url))
updater.dispatcher.add_handler(CommandHandler('Codecademy', Codecademy_url))
updater.dispatcher.add_handler(CommandHandler('AlgoExpert', AlgoExpert_url))
updater.dispatcher.add_handler(CommandHandler('Coderbyte', Coderbyte_url))
updater.dispatcher.add_handler(CommandHandler('freeCodeCamp', freeCodeCamp_url))
updater.dispatcher.add_handler(CommandHandler('leetcode', leetcode_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  

   
updater.start_polling()