/*
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
*/
#pragma once

#include "base/const_string.h"

#define TDESKTOP_REQUESTED_ALPHA_VERSION (0ULL)

#ifdef TDESKTOP_ALLOW_CLOSED_ALPHA
#define TDESKTOP_ALPHA_VERSION TDESKTOP_REQUESTED_ALPHA_VERSION
#else // TDESKTOP_ALLOW_CLOSED_ALPHA
#define TDESKTOP_ALPHA_VERSION (0ULL)
#endif // TDESKTOP_ALLOW_CLOSED_ALPHA

// used in Updater.cpp and Setup.iss for Windows
constexpr auto AppId = "{A6D56417-6490-482F-B0EE-7E4369B7B9DF}"_cs;
constexpr auto AppNameOld = "64Gram Desktop"_cs;
constexpr auto AppName = "Nekogram Desktop"_cs;
constexpr auto AppFile = "Nekogram"_cs;
constexpr auto AppVersion = 1000000;
constexpr auto AppVersionStr = "1.0.0";
constexpr auto AppBetaVersion = false;
constexpr auto AppAlphaVersion = TDESKTOP_ALPHA_VERSION;
constexpr auto UpstreamVersion = "7.2.9";