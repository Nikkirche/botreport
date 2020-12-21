package com.example.botreport_android.views

import android.view.View
import moxy.MvpView
import moxy.viewstate.strategy.alias.AddToEndSingle

interface NewsFlowView:MvpView {
    @AddToEndSingle
    fun goToSettings()
}