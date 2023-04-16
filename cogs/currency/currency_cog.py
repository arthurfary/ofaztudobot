import discord
from discord.ext import commands, tasks
import datetime
import json

class Currency(commands.Cog):
    '''
    Cog that handles currency related commands
    '''
    def __init__(self, bot):
        self.bot = bot

        self.path_to_json = "./cogs/currency/curr.json"

        self.currency_data = self.get_data()  # Store currency data in-memory as a dictionary
        self.currency_name = "Gd"

        self.claimed = {}

    def get_data(self):
        try:
            with open(self.path_to_json, "r") as f:
                return json.load(f)

        except FileNotFoundError:
            # If the data file does not exist, initialize with empty dictionaries
            return {}

    def save_data(self):
        with open(self.path_to_json, "w") as f:
            json.dump(self.currency_data, f, indent=4)
   
    def is_user(self, uid) -> bool:
        '''
        returns bool if uid is found in 'users'
        '''

        if uid in self.currency_data['users']:
            return True
        else:
            return False

    def get_uid(self, ctx) -> str:
        '''
        Returns User Id in a string
        '''
        return str(ctx.message.author.id)

    def add_money(self, uid, amount):
        self.currency_data['users'][uid]['money'] += amount

    @commands.command()
    async def cjoin(self, ctx):
        '''
        Cria conta na economia do server
        '''

        uid = self.get_uid(ctx)

        if not self.is_user(uid):
            self.currency_data['users'][uid] = {
                "user_id": uid,
                "money": 1000,
                "last_claimed": None,
                "shares": {}
            }
            self.save_data()
            await ctx.send(':white_check_mark:')
        
        else:
            await ctx.send(':x:')

    @commands.command()
    async def bal(self, ctx):
        '''
        Mostra o dinheiro na sua conta
        '''

        uid = self.get_uid(ctx)
        if self.is_user(uid):
            await ctx.send(f'Your balance is currently: {self.currency_data["users"][uid]["money"]}{self.currency_name}')
        else:
            await ctx.send(f':x:')

    @commands.command()
    async def checkin(self, ctx):
        '''
        Faça o checkin diário para ganhar pontos
        '''

        uid = self.get_uid(ctx)

        if self.is_user(uid):
            now = datetime.datetime.now()
            today = now.date()
            
            last_claimed = self.currency_data['users'][uid]['last_claimed']
        
            if last_claimed is None or datetime.datetime.strptime(last_claimed, '%Y/%m/%d').date() < today:
                self.add_money(uid, 10)
                self.claimed[uid] = today

                today_str = today.strftime('%Y/%m/%d')
                self.currency_data['users'][uid]['last_claimed'] = today_str

                self.save_data()

                await ctx.send('Claimed!')

            else:
                await ctx.send('Already Claimed')

        else:
            await ctx.send('No account found')
    