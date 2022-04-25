#!/usr/bin/env python3.7
# Import the iterm2 python module to provide an interface for communicating with iTerm
import iterm2
import AppKit

# Launch the app
AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm")

async def main(connection):

    app = await iterm2.async_get_app(connection)

    window = app.current_terminal_window

    if window is not None:
        tab = await window.async_create_tab()

        terminal_1 = tab.current_session
        terminal_2 = await terminal_1.async_split_pane(vertical=False)
        terminal_3 = await terminal_1.async_split_pane(vertical=False)
        terminal_4 = await terminal_1.async_split_pane(vertical=True)


        await terminal_1.async_send_text('cd backend\nyarn dev\n')
        await terminal_2.async_send_text('cd frontend\nyarn dev\n')

        
    else:
        # You can view this message in the script console.
        print("Creating window")
        await iterm2.Window.async_create(connection)

iterm2.run_until_complete(main, True)