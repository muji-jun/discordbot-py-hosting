import discord
from discord.ext import commands
from discord.ui import Button, View

class selectOsi(commands.Cog, name="오시를 선택하는 명령어(중복가능)"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def 오시(self, ctx: commands.Context):
        
        #유저 역할 수집
        userRole = ctx.author.roles
        i = 0
        listRole = []
        while i < len(userRole) :
            listRole.append(userRole[i].name)
            i += 1

        #아이디 변수 설정
        id = ctx.author.id

        
        #버튼 디자인
        button1 = Button(label="히메리", style = discord.ButtonStyle.green)
        button2 = Button(label="모모나", style = discord.ButtonStyle.green)
        button3 = Button(label="모모코", style = discord.ButtonStyle.green)
        button4 = Button(label="미쿠루", style = discord.ButtonStyle.green)
        button5 = Button(label="나오", style = discord.ButtonStyle.green)
        button6 = Button(label="히나", style = discord.ButtonStyle.green)
        button7 = Button(label="에리사", style = discord.ButtonStyle.green)
        button8 = Button(label="리리", style = discord.ButtonStyle.green)
        button9 = Button(label="사아라", style = discord.ButtonStyle.green)
        button10 = Button(label="스우", style = discord.ButtonStyle.green)

        if '히메리 오시' in listRole :
            button1 = Button(label="히메리", style = discord.ButtonStyle.gray)
        if '모모나 오시' in listRole :
            button2 = Button(label="모모나", style = discord.ButtonStyle.gray)
        if '모모코 오시' in listRole :
            button3 = Button(label="모모코", style = discord.ButtonStyle.gray)
        if '미쿠루 오시' in listRole :
            button4 = Button(label="미쿠루", style = discord.ButtonStyle.gray)
        if '나오 오시' in listRole :
            button5 = Button(label="나오", style = discord.ButtonStyle.gray)
        if '히나 오시' in listRole :
            button6 = Button(label="히나", style = discord.ButtonStyle.gray)
        if '에리사 오시' in listRole :
            button7 = Button(label="에리사", style = discord.ButtonStyle.gray)
        if '리리 오시' in listRole :
            button8 = Button(label="리리", style = discord.ButtonStyle.gray)
        if '사아라 오시' in listRole :
            button9 = Button(label="사아라", style = discord.ButtonStyle.gray)
        if '스우 오시' in listRole :
            button10 = Button(label="스우", style = discord.ButtonStyle.gray)                                       
        

        #버튼 콜백 함수
        async def button_callback1(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '히메리 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '히메리 오시' in listRole :
                    await interaction.response.send_message("이미 '히메리 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("히메리를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)
                
        async def button_callback2(interaction:discord.Interaction):
            if interaction.user.id == id :

                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '모모나 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '모모나 오시' in listRole :
                    await interaction.response.send_message("이미 '모모나 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("모모나를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)

        async def button_callback3(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '모모코 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '모모코 오시' in listRole :
                    await interaction.response.send_message("이미 '모모코 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("모모코를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)

        async def button_callback4(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '미쿠루 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '미쿠루 오시' in listRole :
                    await interaction.response.send_message("이미 '미쿠루 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("미쿠루를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)

        async def button_callback5(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '나오 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '나오 오시' in listRole :
                    await interaction.response.send_message("이미 '나오 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("나오를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)

        async def button_callback6(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '히나 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '히나 오시' in listRole :
                    await interaction.response.send_message("이미 '히나 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("히나를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)  

        async def button_callback7(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '에리사 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '에리사 오시' in listRole :
                    await interaction.response.send_message("이미 '에리사 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("에리사를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)
                
        async def button_callback8(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '리리 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '리리 오시' in listRole :
                    await interaction.response.send_message("이미 '리리 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("리리를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)
                
        async def button_callback9(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '사아라 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '사아라 오시' in listRole :
                    await interaction.response.send_message("이미 '사아라 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("사아라를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)
                
        async def button_callback10(interaction:discord.Interaction):
            if interaction.user.id == id :
    
                userRole = ctx.author.roles
                i = 0
                listRole = []
                while i < len(userRole) :
                    listRole.append(userRole[i].name)
                    i += 1

                roleName = '스우 오시'
                member = ctx.author
                checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                if '스우 오시' in listRole :
                    await interaction.response.send_message("이미 '스우 오시' 역할을 보유 중입니다.\r역할을 회수합니다.")
                    await member.remove_roles(checkRole)

                    #DD 해제를 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1   

                    #DD 해제
                    if 'DD' in listRole and lenRole <= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("단오시가 되었습니다.\rDD 역할을 회수합니다.")
                        await member.remove_roles(checkRole)

                else :
                    await interaction.response.send_message("스우를 오시로 선택하셨습니다.\r역할을 부여합니다.")
                    await member.add_roles(checkRole)
                    
                    #DD 설정을 위한 유저 역할 수집
                    userRole = ctx.author.roles
                    i = 0
                    listRole = []
                    while i < len(userRole) :
                        listRole.append(userRole[i].name)
                        i += 1
                    lenRole = len(userRole)

                    #특수역할 확인
                    if '관리자' in listRole :
                        lenRole -= 1
                    if 'Server Booster' in listRole :
                        lenRole -= 1  

                    #DD 부여
                    if 'DD' not in listRole and lenRole >= 3 :
                        roleName = 'DD'
                        checkRole = discord.utils.get(ctx.guild.roles, name=roleName)
                        await ctx.send("오시를 2명 이상 선택하셨습니다.\rDD 역할을 부여합니다.")
                        await member.add_roles(checkRole)    
                
        #버튼 콜백 시 가동 함수 지정
        button1.callback = button_callback1
        button2.callback = button_callback2
        button3.callback = button_callback3
        button4.callback = button_callback4
        button5.callback = button_callback5
        button6.callback = button_callback6
        button7.callback = button_callback7
        button8.callback = button_callback8
        button9.callback = button_callback9
        button10.callback = button_callback10

        #버튼 시각화
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)
        view.add_item(button7)
        view.add_item(button8)
        view.add_item(button9)
        view.add_item(button10)

        #임베드 출력
        await ctx.send(embed = discord.Embed(title='오시를 선택해주세요.',
        description="원하시는 멤버를 선택하시면 자동으로 역할이 부여됩니다. \r이미 오시인 멤버를 선택하시면 역할이 해제됩니다.\r\r2명 이상 선택시 DD역할이 부여됩니다.", 
        colour=discord.Colour.blue()), view=view)    


async def setup(bot: commands.Bot):
    await bot.add_cog(selectOsi(bot))