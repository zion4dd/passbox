class Helptext:
    hello = ['Good day!', 'Nice to see you!', 'Can I help you?', 'It will be our secret..', 
            'They are watching you..', 'Even the walls have ears.', 'Lets hide something..', 'Watch your back!',
            'The paranoid is never entirely mistaken. -Sigmund Freud', 
            'Just because youre paranoid doesnt mean they arent after you. -Kurt Cobain',
            'I wanna smoke pot, but I cant, cause Im too paranoid. -Drew Berrymore',
            'Its amazing where the paranoid mind can take you. -Bill Ayers']

    help_text = """Data storage: 'passbox.bin'.\n
    Load your data:\n- enter 'key'\n- press 'load'.\n
    Add entry:\n- enter 'pin', 'app', 'login', 'pass'\n- press 'add'.\n
    Delete entry:\n- enter 'pin', 'app'\n- press 'del'.\n
    Change 'key':\n- encrypt data with your old 'key'\n- enter new 'key' and 'pin'\n- press 'add'.\n\n
    ***Enjoy it!***"""

    help_text_1 = """Welcome to passbox!\n
    This app keeps your login/pass encrypted and safe.\n
    To begin you need to create storage.\n\n
    Set your 'key' and 'pin'. Than press 'new'.\n\n
    Key format: any symbols.\n
    Pin format: 4 digits! (example: 1234)\n\n
    NOTICE: you CANNOT change your 'pin'!\n
    Cause 'pin' is your storage file ID.\n"""

    help_text_2 = """Storage file 'passbox.bin' was successfully created!\n\n
    All your entries will be stored in this file.\n
    Now you can add and delete entries.\n
    Enter 'key' to encrypt your data.\n\n
    Add entry: enter 'app', 'login', 'pass' and press 'add'.\n
    Delete entry: enter 'app' and press 'del'.\n\n
    'Pin' is used for add and delete operations. It CANNOT be changed.\n
    'Pin' can be set only if you delete your storage and create new.\n\n
    Load your data: enter 'key' and press 'load'.\n
    You don't need 'pin' to load and encrypt.\n\n
    Change 'key': encrypt data with your old 'key', enter new 'key' and 'pin', than press 'add'."""
