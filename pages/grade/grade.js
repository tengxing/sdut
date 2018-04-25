//logs.js
const util = require('../../utils/util.js')

Page({
  data: {
    grades: [],
    name: ''
  },
  onLoad: function () {
    this.setData({
      grades: getApp().globalData.grades
    })
  }
})
