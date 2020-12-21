package com.example.botreport_android.entities

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class LiveNews (
    @SerializedName("live-news")
    @Expose
    var liveNews:List<LiveEvent> = arrayListOf()
)