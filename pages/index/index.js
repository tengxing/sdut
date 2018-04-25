//index.js
//获取应用实例
const app = getApp()

Page({
  globalData:{
    name:"tengxing"
  },
  data: {
    stdId: '',
    userInfo: {},
    hasUserInfo: false,
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../grade/grade'
    })
  },
  stdId: function (e) {
    var that = this;
    that.setData({
      stdId: e.detail.value
    })
  },
  //chaxun 
  getGrade: function() {
    var user_info = {}
    var that = this;
    var stdId = that.data.stdId;
    wx.request({
      method: 'GET',
      url: 'https://yjxxclub.cn/jwch/info/?std_id='+stdId,
      data: {
        'stdId': that.data.stdId,
      },
      header: { 'content-type': 'application/json' },
      success: function (res) {
        user_info = res.data; 
        getApp().globalData.grades = user_info.subject_info
        console.info(user_info);
        wx.showModal({
          title: '查询结果',
          icon:'success',
          content: '姓名:' + user_info.name 
          + "\r\n学号:" + user_info.stdId
          + "\r\n性别:" + user_info.sex
          + "\r\n专业:" + user_info.profession
          + "\r\n班级:" + user_info.class

          ,
          success: function (res) {1
            if (res.confirm) {
              console.log('用户点击确定')
            } else if (res.cancel) {
              console.log('用户点击取消')
            }
          }
        })
      },
    })
  },

  onLoad: function () {
    var that = this;
    wx.login({
      success: function (e) {
        console.info("登陆返回:" + e.code)
        wx.getUserInfo({
          success: function (res) {
            var simpleUser = res.userInfo;
            console.log(simpleUser.nickName);
            that.setData({
              userInfo: simpleUser,
              hasUserInfo: true
            })
          },
          fail: function () {
            console.info("不授權，不让你使用");
            /**
             * wx.navigateBack({
              delta: -1
            })
            wx.clearStorage();
             */
          }
        });
      }
    });
  }
})
