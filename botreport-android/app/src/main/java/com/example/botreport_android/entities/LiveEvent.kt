package com.example.botreport_android.entities

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class LiveEvent(

    @SerializedName("text")
    @Expose
    var text: String,
    @SerializedName("data")
    @Expose
    var data: String
)