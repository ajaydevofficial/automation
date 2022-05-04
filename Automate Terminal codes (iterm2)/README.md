# Automate Terminal Codes

Always running codes required to start pojects that you work on daily can be a very frustruating task. Ever had to run all your codes again and again after restarts and shutdowns. Have multiple repos/projects to run at the same time (I have around 9 projects to run daily..)

The aim of this single file code is to automate this task for you

You might want to tweak this a little bit ofr Ubuntu/Windows as this code was tested only on MacOS

## What do you have to do?
iTerm (https://iterm2.com/downloads/stable/latest) should be installed and Ensure the Python API is enabled in iTerm2's preferences ( iTerm2 -> Preferences -> Magic -> select Enable Python API )

It's simple.. open the iterm_automate.py file ans customize it from line no.16. It might take 10 minutes but it's worth it

## Want to create a new tab?

```
tab = await window.async_create_tab()
```

## Want to split multiple terminals in the same tab ?

1. Create your first terminal session (one large terminal)
    ```
    terminal_1 = tab.current_session
    ```
2. Create a vertical split
    ```
    terminal_2 = terminal_1.async_split_pane(vertical=True)
    ```
3. Create a horizontal split on any of the tabs
    ```
    terminal_3 = terminal_1.async_split_pane(vertical=False)
    ```
    or
    ```
    terminal_3 = terminal_2.async_split_pane(vertical=False)
    ```
4.  Running a command in ```terminal_1```
    ```
    await terminal_1.async_send_text('Your command with \n separated wherever you want to press enter key')
    ```

## Run the script and see it doing the hardowrk for you

```
python3 script_name.py
```
