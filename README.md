# user_name_restriction
A simple module for Odoo 16 to limit a bot attack with random user names

After some weeks of my website being attacked by a bot, which created fake user accounts with random names using random upper and lowercase letters, but using real e-mail accounts (probably from a hacked place), I posted my issue in the Odoo forums. 
After some days, looks like I wasn't the only one to suffer this attack. In my case, I had to manually delete up to 40-50 fake accounts. 
Being annoying, that wasn't the most worrying thing, as my domain could be included as a spammer, and that's a big problem for my business.
Some forum users gave some ideas and I decided to give it a try.

As a non professional programmer or Odoo collaborator, I have limited knowledge of Odoo related coding, so I learned that AI could help.
I was pointed out by some Odoo forums user that the random usernames had multiple uppercase letters, so some coding could be written to avoid more than one capital letter per word in the name field, so I asked ChatGPT to write an Odoo16 module to avoid this.

After some manual code tweaking, I could get a fully installable and functional module that could restrict the use of uppercase letters in the field name, either in the frontend or in the backend of my version of Odoo

My Odoo website and backend is using the standard field names and forms, so the user should change or adapt the module to their needs.

As I stated before, I am not a professional developer and I cannot be held responsible for the loss of third-party data, so I strongly recommend to test the module in a sandbox where you have your page in or make a backup of the data before installing it

To install it, like normal modules. Add the folder inside the zip file I sent you to the addons (or custom addons) folder in your odoo drive, go to the odoo applications section, update the applications and look for user_name_restriction. There you can install the module. For security, once installed, restart the odoo service or the entire server and test its operation.

This module was specially made for Odoo 16, but I see no reason for it not to work with other versions. Do your research first.

I hope this module helps you as much as it does me.
Good luck!
