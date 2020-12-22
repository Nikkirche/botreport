package com.example.botreport_android.ui

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button

import androidx.lifecycle.lifecycleScope
import com.example.botreport_android.R
import com.example.botreport_android.main.MainActivity
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import moxy.MvpAppCompatFragment
import reactivecircus.flowbinding.android.view.clicks
@AndroidEntryPoint
class SettingsFlowFragment : Fragment(){
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_settings_flow, container, false)
        view.findViewById<Button>(R.id.backFromSettings)
            .clicks()
            .onEach {
                (activity as MainActivity).supportFragmentManager.popBackStack()
            }
            .launchIn(viewLifecycleOwner.lifecycleScope)

        return view
    }

}