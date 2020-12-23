# from test_case.launch import App
import allure
from airtest.core.api import *
import pytest

img_dir = '../case_img/offical'
logger = App.logger


@allure.feature('测试官方渠道_v{}'.format(App.config['version']))
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.resolution = (2340, 1080)
        cls.poco = App.start(App.config['version'], 'offical')

    @allure.title("新手教程")
    def test_guide(self):
        # 朕已阅
        wait(Template('{}/close_note.png'.format(img_dir), resolution=self.resolution), timeout=20)
        touch(Template('{}/close_note.png'.format(img_dir), resolution=self.resolutio))
        # # 快速注册
        self.poco(text='快速注册').click()
        self.poco(name='com.hulai.hlsg3d.gw:id/hl_cb_protocol').click()
        self.poco(text='确认').click()
        self.poco(name='com.hulai.hlsg3d.gw:id/Hl_Sdk_Close2').click()
        # 开始游戏
        touch(Template('{}/start_game.png'.format(img_dir), resolution=self.resolution))
        # 创建角色进入游戏
        touch(Template('{}/enter_game.png'.format(img_dir), resolution=self.resolution))
        # 貂蝉:
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 全军出击
        touch(Template('{}/all_fight.png'.format(img_dir), resolution=self.resolution))
        # 响应集结
        touch(Template('{}/gather.png'.format(img_dir), resolution=self.resolution))
        # 董卓：老夫乃大汉相国...
        wait(Template('{}/npc_dongzhuo.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        self.poco().click()
        touch(Template('{}/skip_fight.png'.format(img_dir), resolution=self.resolution, target_pos=6))
        # 点击元宝
        wait(Template('{}/gold.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/gold.png'.format(img_dir), resolution=self.resolution))
        # 沙摩柯：贼人来犯...
        wait(Template('{}/npc_shamoke.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 点击确认
        touch(Template('{}/ensure1.png'.format(img_dir), resolution=self.resolution,target_pos=9))
        # 点击李儒军团
        touch(Template('{}/enemy_liru.png'.format(img_dir), resolution=self.resolution))
        # 地图上点征讨
        touch(Template('{}/map_conquest.png'.format(img_dir), resolution=self.resolution))
        # 队伍界面点征讨
        touch(Template('{}/team_conquest.png'.format(img_dir), resolution=self.resolution))
        # 装备给主公
        wait(Template('{}/npc_guide.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/equip_lord.png'.format(img_dir), resolution=self.resolution))
        # 点击空地
        touch(Template('{}/space_area.png'.format(img_dir), resolution=self.resolution))
        # 地图上点出征
        touch(Template('{}/map_conquest1.png'.format(img_dir), resolution=self.resolution, target_pos=6))
        # 队伍界面点出征
        touch(Template('{}/team_conquest.png'.format(img_dir), resolution=self.resolution))
        # 貂蝉：此次收复领地...
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 点击武将
        touch(Template('{}/general.png'.format(img_dir), resolution=self.resolution))
        # 武将界面点击装备
        touch(Template('{}/equipment.png'.format(img_dir), resolution=self.resolution, target_pos=8))
        # 强化1级
        touch(Template('{}/strengthen_equipment.png'.format(img_dir), resolution=self.resolution, target_pos=9))
        time.sleep(5)
        touch(Template('{}/strengthen_equipment.png'.format(img_dir), resolution=self.resolution, target_pos=9))
        # 点击返回
        touch(Template('{}/back_5.png'.format(img_dir), resolution=self.resolution, target_pos=1))
        # 点击空地
        touch(Template('{}/space_area.png'.format(img_dir), resolution=self.resolution))
        # 地图上点出征
        touch(Template('{}/map_conquest.png'.format(img_dir), resolution=self.resolution))
        # 队伍界面点出征
        touch(Template('{}/team_conquest.png'.format(img_dir), resolution=self.resolution))
        # 貂蝉：诸梦游请求一起进军，讨伐董卓...
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 招募
        touch(Template('{}/recruit.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/advanced_recruit.png'.format(img_dir), resolution=self.resolution, target_pos=8))
        # 点击卡牌继续
        wait(Template('{}/card.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/card.png'.format(img_dir), resolution=self.resolution))
        wait(Template('{}/general_ensure.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/general_ensure.png'.format(img_dir), resolution=self.resolution, target_pos=9))
        # 返回主界面
        touch(Template('{}/back_2.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/back_2.png'.format(img_dir), resolution=self.resolution))
        # 布阵
        touch(Template('{}/formation.png'.format(img_dir), resolution=self.resolution))
        wait(Template('{}/npc_guide.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 更换武将
        touch(Template('{}/exchange_general.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/exchange_btn.png'.format(img_dir), resolution=self.resolution, target_pos=9))
        touch(Template('{}/back_6.png'.format(img_dir), resolution=self.resolution))
        if exists(Template('{}/hide_icon.png'.format(img_dir), resolution=self.resolution)):
            touch(Template('{}/hide_icon.png'.format(img_dir), resolution=self.resolution))
            touch(Template('{}/back_6.png'.format(img_dir), resolution=self.resolution))

        # 貂蝉：兴霸将军加入，我军如虎添翼...
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 点击叛军大营
        touch(Template('{}/enemy_camp.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/map_conquest.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/team_conquest.png'.format(img_dir), resolution=self.resolution))
        # 指导领取战利品
        wait(Template('{}/npc_guide.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/reward.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/receive.png'.format(img_dir), resolution=self.resolution, target_pos=8))
        # 貂蝉：此次征讨董卓...
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 赶快升官
        wait(Template('{}/npc_guide.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/start_union.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/promotion.png'.format(img_dir), resolution=self.resolution))
        wait(Template('{}/promotion_notice.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/i_know.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/back_4.png'.format(img_dir), resolution=self.resolution))
        # 貂蝉：如今主公名传天下...
        wait(Template('{}/npc_diaochan.png'.format(img_dir), resolution=self.resolution))
        self.poco().click()
        # 确认所选阵营
        touch(Template('{}/confirm_faction.png'.format(img_dir), resolution=self.resolution))
        wait(Template('{}/union_invitation.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/ensure2.png'.format(img_dir), resolution=self.resolution))
        # 点击联盟
        touch(Template('{}/union.png'.format(img_dir), resolution=self.resolution))
        # 联盟指引
        sleep(3)
        self.poco().click()
        touch(Template('{}/back_2.png'.format(img_dir), resolution=self.resolution))
        # 征讨贼寇并领取奖励
        touch(Template('{}/mission_fight_enemy.png'.format(img_dir), resolution=self.resolution, target_pos=8))
        touch(Template('{}/map_conquest.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/team_conquest.png'.format(img_dir), resolution=self.resolution))
        touch(Template('{}/mission_fight_enemy.png'.format(img_dir), resolution=self.resolution, target_pos=8))
        self.poco().click()

    def assert_money(self, exp_gold, exp_money):
        touch(Template('{}/{}_gold.png'.format(img_dir, exp_gold), resolution=self.resolution))
        wait(Template('{}/pay_now.png'.format(img_dir), resolution=self.resolution))
        gold = int(self.poco(name='com.hulai.hlsg3d.gw:id/hl_tv_itemName').get_text().strip("元宝"))
        money = int(self.poco(name='com.hulai.hlsg3d.gw:id/hl_tv_amount').get_text().strip("￥"))
        assert gold == exp_gold
        assert money == exp_money
        self.poco(text='立即支付').click()
        wait(Template('{}/alipay.png'.format(img_dir), resolution=self.resolution))
        try:
            if self.poco(text='立即下载支付宝').exists():
                logger.info('----------充值{}元宝调起SDK测试完成----------'.format(exp_gold))
        except Exception:
            raise logger.info('----------充值{}元宝调起SDK测试失败----------'.format(exp_gold))
        # self.poco(text='微信支付').click()
        # assert_exists(Template('{}/wx_pay.png'.format(img_dir), resolution=self.resolution))
        keyevent("4")
        # self.poco(text='放弃').click()
        # logger.info('----------充值{}元宝调起SDK测试完成----------'.format(exp_gold))
        self.poco(name='com.hulai.hlsg3d.gw:id/hl_btn_close').click()

    def test_pay(self):
        # touch(Template('{}/top_up.png'.format(img_dir), resolution=self.resolution))
        self.assert_money(60, 6)
        # self.assert_money(300, 30)
        # self.assert_money(980, 98)
        # self.assert_money(1280, 128)
        # self.assert_money(3280, 328)
        # self.assert_money(6480, 648)

    # @allure.title('测试注册')
    # def test_register_quickly(self):
    #     id_num = '123456'
    #     name = '张三'
    #     self.poco(text='快速注册').wait()
    #     self.poco(name='com.hoolai.sanguo2:id/hl_quickRegister').click()
    #     if self.poco(text='身份证号码').exists():
    #         self.poco(text='身份证号码').set_text(id_num)
    #         self.poco(text='真实姓名').set_text(name)
    #         self.poco(text='提交认证').click()
    #         self.poco(text='返回登陆').click()
    #         self.poco(name='com.hoolai.sanguo2:id/more_user').click()
    #         self.poco(name='com.hoolai.sanguo2:id/option_item_del').click()
    #
    #     time.sleep(5)
    #
    # @allure.title("测试登录")
    # def test_login_on(self):
    #     username = 'hulai123'
    #     pwd = 'test123'
    #     self.poco(text='胡莱通行证登录').click()
    #     self.poco(name='com.hoolai.sanguo2:id/hl_login_edit_account').set_text(username)
    #     self.poco(name='com.hoolai.sanguo2:id/hl_login_edit_pwd').set_text(pwd)
    #     self.poco(text='登录').click()
    #
    # time.sleep(5)
    #
    # @allure.title('测试用户名注册')
    # def test_username_register(self):
    #     username = 'hulai123'
    #     pwd = 'test123'
    #     self.poco(text='用户名注册').click()
    #     self.poco(name='com.hoolai.sanguo2:id/hl_login_edit_account').set_text(username)
    #     self.poco(name='com.hoolai.sanguo2:id/hl_login_edit_pwd').set_text(pwd)
    #     self.poco(text='注册新号').click()

    @classmethod
    def teardown_class(cls):
        App.quit('offical')
