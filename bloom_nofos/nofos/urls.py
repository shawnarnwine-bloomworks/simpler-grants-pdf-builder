from django.urls import path

from . import views

app_name = "nofos"
urlpatterns = [
    path("", views.NofosListView.as_view(), name="nofo_index"),
    path("import", views.nofo_import, name="nofo_import"),
    path("<int:pk>/delete", views.NofosDeleteView.as_view(), name="nofo_delete"),
    path("<int:pk>/import", views.nofo_import, name="nofo_import_overwrite"),
    path(
        "<int:pk>/import/title",
        views.NofoImportTitleView.as_view(),
        name="nofo_import_title",
    ),
    path(
        "<int:pk>/import/number",
        views.NofoImportNumberView.as_view(),
        name="nofo_import_number",
    ),
    path(
        "<int:pk>/import/coach",
        views.NofoImportCoachView.as_view(),
        name="nofo_import_coach",
    ),
    path("<int:pk>", views.NofosDetailView.as_view(), name="nofo_view"),
    path("<int:pk>/edit", views.NofosEditView.as_view(), name="nofo_edit"),
    path(
        "<int:pk>/edit/coach", views.NofoEditCoachView.as_view(), name="nofo_edit_coach"
    ),
    path(
        "<int:pk>/edit/title", views.NofoEditTitleView.as_view(), name="nofo_edit_title"
    ),
    path(
        "<int:pk>/edit/number",
        views.NofoEditNumberView.as_view(),
        name="nofo_edit_number",
    ),
    path(
        "<int:pk>/edit/application-deadline",
        views.NofoEditApplicationDeadlineView.as_view(),
        name="nofo_edit_application_deadline",
    ),
    path(
        "<int:pk>/edit/tagline",
        views.NofoEditTaglineView.as_view(),
        name="nofo_edit_tagline",
    ),
    path(
        "<int:pk>/edit/opdiv",
        views.NofoEditOpDivView.as_view(),
        name="nofo_edit_opdiv",
    ),
    path(
        "<int:pk>/edit/agency",
        views.NofoEditAgencyView.as_view(),
        name="nofo_edit_agency",
    ),
    path(
        "<int:pk>/edit/subagency",
        views.NofoEditSubagencyView.as_view(),
        name="nofo_edit_subagency",
    ),
    path(
        "<int:pk>/edit/theme",
        views.NofoEditThemeView.as_view(),
        name="nofo_edit_theme",
    ),
    path(
        "<int:pk>/edit/cover",
        views.NofoEditCoverView.as_view(),
        name="nofo_edit_cover",
    ),
    path(
        "<int:pk>/edit/subsection/<int:subsection_pk>",
        views.nofo_subsection_edit,
        name="subsection_edit",
    ),
    path("<int:pk>/print/", views.PrintNofoAsPDFView.as_view(), name="print_pdf"),
]
