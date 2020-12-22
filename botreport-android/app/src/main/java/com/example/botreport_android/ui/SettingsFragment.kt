package com.example.botreport_android.ui

import android.os.Bundle
import androidx.preference.Preference
import androidx.preference.PreferenceFragmentCompat
import androidx.preference.PreferenceManager
import androidx.preference.SwitchPreference
import com.example.botreport_android.R
import com.example.botreport_android.util.ThemeHelper
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SettingsFragment : PreferenceFragmentCompat() {
    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        setPreferencesFromResource(R.xml.root_preferences, rootKey)
        findPreference<SwitchPreference>("themePref")?.setOnPreferenceChangeListener(
            object : Preference.OnPreferenceChangeListener {
                override fun onPreferenceChange(preference: Preference, newValue: Any): Boolean {
                    val themeOption:String
                    if(newValue==true){
                         themeOption = "dark"

                    }
                    else{
                        themeOption = "white"
                    }
                    PreferenceManager.getDefaultSharedPreferences(context).edit().putString("theme",themeOption).apply()
                    ThemeHelper.applyTheme(themeOption)
                    return true
                }
            })
    }

    }




