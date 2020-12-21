package com.example.botreport_android.presenter

import android.view.View
import com.example.botreport_android.views.NewsFlowView
import moxy.MvpPresenter
import javax.inject.Inject

class NewsFlowPresenter @Inject constructor() : MvpPresenter<NewsFlowView>() {
    fun openSettings(){
        viewState.goToSettings()
    }


}