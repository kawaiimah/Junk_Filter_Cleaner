# Junk_Filter_Cleaner
This is just a little bugbear of mine - I get really irritated when I encounter the following:
- I receive junk email from Alice@spancompanyX.com. I use Outlook context menu to block sender.
- Next day, I receive junk email from Bob@spancompanyX.com. I use Outlook context menu to block sender again.
- Next next day, I receive junk email from Charlie@spamcompanyX.com. I realise I need to block @spancompanyX.com. I sigh at the lack of context menu option. I click thru multiple menus to get to the junk email filter. I manually add @spamcompanyX.com to the filter.

I've searched high and low, Outlook simply does not include a simple one-click option to block a sender's domain!

So my workaround is to use this little bit of code every couple of months. It takes the current junk email filter list I have exported from Outlook and outputs a text file which contains domains only, which I can then import back into Outlook.
