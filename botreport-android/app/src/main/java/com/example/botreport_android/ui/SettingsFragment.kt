package com.example.botreport_android.ui

import android.os.Bundle
import androidx.preference.PreferenceFragmentCompat
import com.example.botreport_android.R
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class SettingsFragment : PreferenceFragmentCompat() {

    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        setPreferencesFromResource(R.xml.root_preferences, rootKey)
    }

}