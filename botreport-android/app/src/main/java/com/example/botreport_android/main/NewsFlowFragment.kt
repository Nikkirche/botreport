package com.example.botreport_android.main

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import androidx.fragment.app.Fragment
import androidx.fragment.app.add
import androidx.fragment.app.commit
import androidx.viewpager2.adapter.FragmentStateAdapter
import androidx.viewpager2.widget.ViewPager2
import com.example.botreport_android.R
import com.example.botreport_android.presenter.NewsFlowPresenter
import com.example.botreport_android.ui.ArticleFeedFragment
import com.example.botreport_android.ui.LiveNewsFeedFragment
import com.example.botreport_android.views.NewsFlowView
import com.google.android.material.tabs.TabLayout
import com.google.android.material.tabs.TabLayoutMediator
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.flow.onEach
import moxy.ktx.moxyPresenter

import reactivecircus.flowbinding.android.view.clicks
import javax.inject.Inject
import javax.inject.Provider
import androidx.lifecycle.lifecycleScope
import com.example.botreport_android.presenter.MainPresenter
import com.example.botreport_android.ui.SettingsFlowFragment
import kotlinx.coroutines.flow.launchIn
import moxy.MvpAppCompatFragment

@AndroidEntryPoint
class NewsFlowFragment : MvpAppCompatFragment(), NewsFlowView {
    @Inject
    lateinit var presenterProvider: Provider<NewsFlowPresenter>
    private val presenter: NewsFlowPresenter by moxyPresenter { presenterProvider.get() }

    private lateinit var viewAdapter: ViewAdapter
    private lateinit var viewPager: ViewPager2
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view: View = inflater.inflate(
            R.layout.news__flow_fragment,
            container, false
        )
        val buttonToSetting = view.findViewById<ImageButton>(R.id.button_to_settings)

        buttonToSetting.clicks().onEach {
            presenter.openSettings()
        }.launchIn(viewLifecycleOwner.lifecycleScope)

        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewAdapter = ViewAdapter(this)
        viewPager = view.findViewById(R.id.pager)
        viewPager.adapter = viewAdapter
        val tabLayout: TabLayout = view.findViewById(R.id.menu)
        TabLayoutMediator(tabLayout, viewPager) { tab, position ->
            if (position == 0) {
                tab.text = "События"
            } else {
                tab.text = "Статьи "
            }
            viewPager.setCurrentItem(tab.position, true)
        }.attach()
    }

    override fun goToSettings() {
        (activity as MainActivity).supportFragmentManager.commit {
            setReorderingAllowed(true)
            add<SettingsFlowFragment>(R.id.main)
            addToBackStack("settings")
        }
    }

}

class ViewAdapter(fragment: Fragment) : FragmentStateAdapter(fragment) {

    override fun getItemCount(): Int = 2

    override fun createFragment(position: Int): Fragment {
        // Return a NEW fragment instance in createFragment(int)
        if (position == 0) {
            return LiveNewsFeedFragment()
        } else {
            return ArticleFeedFragment()
        }
    }
}
