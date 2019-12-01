         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
# cloudmart

credits for login form layout: https://codepen.io/T-P/pen/bpWqrr
cart inspired by: https://dribbble.com/shots/5039057-Shopping-cart-V2

errors: 
1. static media wont show up after user register > redirected to <url>/accounts/
    a) either fix routing to <url>/
    b) get static media to work on <url>/accounts/

2. non-user able to view individual product page but registered user cant
    a) error with {%user auth%} part