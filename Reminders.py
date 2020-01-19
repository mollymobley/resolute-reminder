from discord.ext import tasks, commands
from datetime import datetime, now

class Reminder():
    def __init__(self, author: str, message: str, time: datetime):
        self.author = author
        self.message = message
        self.time = time

    def isDue():
        return self.time < now()
    
    def notifyAuthor():
        pass

class ReminderManager(commands.Cog):
    def __init__(self):
        self.reminders = []
        self.checkAll.start()

    def cog_unload(self):
        self.checkAll.cancel()

    @tasks.loop(minutes=1.0)
    async def checkAll(self):
        for reminder in self.reminders:
            if reminder.isDue():
                reminder.notifyAuthor():

    def to_datetime(stringtime):
        pass
        # TODO steal that one guys stuff

    @commands.command(name = "remindme")
    async def createReminder(self, ctx, message: str, time: to_datetime):
        newReminder = Reminder(message, time)
        self.reminders.append(newReminder)
        ctx.send("Reminder containing: '{0}', set for {1}".format(message, time))