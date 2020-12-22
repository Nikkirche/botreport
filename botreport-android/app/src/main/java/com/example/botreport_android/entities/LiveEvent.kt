package com.example.botreport_android.entities

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class LiveEvent(

    @SerializedName("text")
    @Expose
    var text: String,
    @SerializedName("generatedtext")
    @Expose
    var generatedText: String,
    @SerializedName("player")
    @Expose
    var player: String,
    @SerializedName("match")
    @Expose
    var match: String,
    @SerializedName("data")
    @Expose
    var data: String,
    @SerializedName("leagua")
    @Expose
    var leagua: String,
    @SerializedName("type")
    @Expose
    var type: String
)