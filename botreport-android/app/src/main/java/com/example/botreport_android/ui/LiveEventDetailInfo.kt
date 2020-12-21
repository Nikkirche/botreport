package com.example.botreport_android.ui

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.botreport_android.R
import com.example.botreport_android.databinding.FragmentLiveEventDetailInfoBinding
import com.example.botreport_android.databinding.FragmentTagBinding
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class LiveEventDetailInfo : Fragment() {
    private var _binding:FragmentLiveEventDetailInfoBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_live_event_detail_info, container, false)
    }

}