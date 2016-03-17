# Robo
Robo is an anonymous image board application in the vane of sites like 4chan and lainchan.

# Robo is *NOT* ready for production. Repeat, *DO NOT USE IN PRODUCTION*

## Structure
Robo has 4 main modules; index, board, thread, and post.

* index:
    * This is the 'homepage' of the application.
    * Lists currently available boards as links.
    * Lists info for each board.

* board:
    * Includes Board model which is pretty much self explanatory.
    * Very simple implementation. Easily extendable through adding fields to the Board model or subclassing the Board model.
    * Basic view handles displaying board basic info and threads for specific board.
    * Can easily alter board display through editing ```board/templates/board/single_thread.html```
    * Board list is display as an unordered list of links using a simple template tag contained in ```board/templatetags/board_list.py```. Template is located at ```board/templates/board/tag_board_list.html```.
    * Create new boards through the standard Django admin. Users cannot create new boards. In future versions, there may be an option to allow users to create new boards.
    
* thread:
    * Includes basic Thread model which has a relationship to parent board.
    * Includes relationship to child posts.
    * Includes single thread view which has a simple form to allow creation of new threads.
    * Single thread view lists child posts.
    * Can moderate threads through Django admin. Future versions will allow live moderation.
    
* post:
    * Includes basic Post model which has a relationship to parent thread.
    * Posts can be children of other posts.
    * Posts rendered in single thread view have a link to their parent. Future versions will include inline threading(nested replies).
    * Each post has it's own reply form that uses a small amount of JavaScript to show or hide the form. This javascript is included in ```static/site/js/main.js```.
    
## Styling
Robo uses skeleton as a basic CSS framework. This can be changed with a little bit of work. You will need to replace ```static/skeleton``` and it's child directories and files with whatever CSS framework you would like to use. Then you will need to go through the templates and replace the HTML element classes with whatever classes make sense with your chosen framework.

## Contributing
Robo really needs contributors. I am only one person, and this project needs a lot of work. I am willing to put in the work myself, but I feel like the quality of the application will be greatly improved if more brains get involved. As it currently stands, Robo doesn't really know what it is. Should Robo be a framework for image board applications, or should Robo make all the decisions and be deployed and foster it's own community? This is a question I can't answer myself.

## Goals for the future

* Better security:
    * As it stands, Robo is extremely insecure, especially when it comes to form validation. 
    * Add unit tests and functional tests. This is something I aim to work on next.
* More functionality:
    * Add image lookups and exif data for images.
    * Add support for webms and audio files.
    * Add tripcode support.
    * Add better moderation tools.