package com.example.botreport_android

import android.app.Application
import android.util.Log
import androidx.preference.PreferenceManager
import com.example.botreport_android.util.ThemeHelper
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class BotreportApp:Application(){
    override fun onCreate() {
        super.onCreate()
        val sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this)
        val themePref = sharedPreferences.getString("theme", ThemeHelper.DEFAULT_MODE)
        Log.d("theme",themePref!!::class.simpleName.toString())
        ThemeHelper.applyTheme(themePref)
    }
}
