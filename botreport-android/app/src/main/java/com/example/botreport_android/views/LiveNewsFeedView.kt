package com.example.botreport_android.views

import com.example.botreport_android.entities.LiveEvent
import moxy.MvpView
import moxy.viewstate.strategy.alias.AddToEndSingle

interface LiveNewsFeedView:MvpView{
    @AddToEndSingle
    fun setInAdapter(result: ArrayList<LiveEvent>)

}